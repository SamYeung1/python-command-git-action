import sys

from tasks.call_api_command import CallAPICommand


def main():
    tasks = list([CallAPICommand(sys.argv)])
    for task in [task for task in tasks if task.name == sys.argv[1]]:
        task.execute()


if __name__ == '__main__':
    main()
