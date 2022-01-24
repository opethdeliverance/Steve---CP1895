
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
    total_animals = str(how_many(animals))
    print (('There are ' + total_animals + ' animals'))




if __name__ == '__main__':
  main()

