
def how_many(animals):
    total = 0
    for item in animals.values():
        total += len(item)
    return total




def main():
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    print(animals.values())
    print (how_many(animals))




if __name__ == '__main__':
  main()

