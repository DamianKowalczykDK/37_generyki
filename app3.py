
class Words(str):
    def __len__(self) -> int:
        return len(self.split())

def inspect(text: str) -> None:
    print(f'{text.upper()} has length: {len(text)}')


def main() -> None:
    inspect('Ala ma kota')
    inspect(Words('Ala ma kota'))

if __name__ == '__main__':
    main()