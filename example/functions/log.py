from UseFul import func_log
from logbook.handlers import StreamHandler
from sys import stdout

StreamHandler(stdout).push_application()


@func_log
def check(name, lastname, age=30):
    check.log.info(f'{name=} {lastname=} {age=} {check.__dict__=}')
    return (name, lastname, age,)


print(check("hamed", "knew", 18.6))
