
# Реализуйте здесь простую машину состояний (State Machine).
# Функция должна принимать текущее состояние и событие,
# и возвращать следующее состояние.

def next_state(state: str, event: str) -> str:
    if state == 'NEW':
        if event == 'PAY_OK':
            return 'PAID'
        elif event in ('PAY_FAIL', 'cancel'):
            return 'CANCELLED'
        else:
            return state
    elif state == 'PAID':
        if event == 'complete':
            return 'DONE'
        elif event in ('cancel', 'PAY_FAIL'):
            return 'CANCELLED'
        else:
            return state
    else:
        return state
