def count_by_var(var: int, max_count:int=500)-> int:
    result = 0

    with open('geeks.txt', 'w+') as file:
        for i in range(max_count):
            result += var
            file.write(f"Count: {i+1}\t"+
                       f"{result}\n")
        return result
