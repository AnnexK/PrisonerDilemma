from parse import get_task
from loader import load_task


def print_pris(P):
    print('Contestants:')
    for i, p in enumerate(P):
        print(f'{i+1}. {p}')


def print_res(places, points):
    print('Tournament results:')
    for i, z in enumerate(zip(places, points)):
        print(f'{i+1}. {z[0]} with {z[1]} loss points')


def main():
    payload = get_task()
    pit, P = load_task(payload)
    print_pris(P)
    places, points = pit.tournament(P)
    print_res(places, points)


if __name__ == "__main__":
    main()
