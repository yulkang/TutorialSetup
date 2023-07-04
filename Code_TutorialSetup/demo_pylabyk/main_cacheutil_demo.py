from pylabyk.localfile import LocalFile


def main():
    localfile = LocalFile('Data/main_cacheutil_demo')
    with localfile.get_cache('demo_simple') as cache:
        cache.set({
            'a': 1,
            'b': 2
        })
    with localfile.get_cache('demo_simple') as cache2:
        a, b = cache2.getdict(['a', 'b'])
        print(f'a: {a}, b: {b}')


if __name__ == '__main__':
    main()