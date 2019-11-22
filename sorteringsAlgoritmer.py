def insertionSort(file):
#den er forkert
    #opretter den fil vi kan rette i, så vi ikke piller ved den originale
    file1 = file.copy()

    #finder længden af listen file1
    length = len(file1)

    #loper gennem alle elementer i listen
    for element in range(1, length):

        #gemmer elementet vi har fat i
        index = file1[element]

        #gemmer det forige element
        i = element-1

        #tjækker at vi ikke er i starten af listen og index er mindre end det forige element
        while i >= 0 and index < file1[i]:

            #byt rundt her
            file1[i+1] = file1[i]
            i -= 1
            file1[i+1] = index

    #retuneres tilbage til dig martin <3 #NoHomoTho
    return file1





def selectionSort(file):
    #opretter den fil vi kan rette i, så vi ikke piller ved den originale
    file1 = file.copy()

    #finder længden af listen file1
    length = len(file1)

    #loper gennem alle elementer i listen
    for element in range(length):

        minIndex = element
        #kører gennem listen fra "element" + 1 af
        #finder den mindste værdi af listen, og gemmer den
        for i in range(minIndex+1, length):
            #tjækker om minIndex er højere end i
            if file1[minIndex] > file1[i]:
                #sæt index til at være i
                minIndex = i

        #efter vi har fundet den mindste værdi bytter vi rundt på element og minIndex.
        #gemmer den ene værdi i holder
        holder = file1[element]
        #bytter rundt på de to værdier
        file1[element] = file1[minIndex]
        file1[minIndex] = holder

    #retuneres tilbage til dig martin <3 #NoHomoTho
    return file1




def bubbleSort(file):

    #opretter den fil vi kan rette i, så vi ikke piller ved den originale
    file1 = file.copy()

    #finder længden af listen file1
    length = len(file1)

    #kører igennem hele listen, og hvert element i listen
    for element1 in range(length):
        for element2 in range(length-1):

            #tjekker om det næste element er lavere en det element vi har fat i
            if file1[element2] > file1[element1] :
                #hvis ja, gemmer vi den ene værdi i holder
                holder = file1[element1]

                #så bytter vi rundt på dem.
                file1[element1] = file1[element2]
                file1[element2] = holder
    #her retunere vi filen file1 til dig martin <3
    return file1




def mergeSort(file):
    def mergeSortT(listToSort):

        #tjækker om listen er længere end en
        if len(listToSort) > 1:

            #split listen i 2
            pivit = len(listToSort)//2

            #gemmer begge halv dele af listen i to nye lister.
            leftlist = listToSort[:pivit]
            rightlist = listToSort[pivit:]

            #se selv hvordan den splitter.
            #print(leftlist)
            #print(rightlist)

            #kalder sig selv igen, med de to lister.
            #laver et loop til de ikke kan splittes udligere.
            mergeSortT(leftlist)
            mergeSortT(rightlist)


            #variabler, som holder styr på hvor lang vi er nået i vores sortering
            leftI = 0
            rightI = 0
            tempI = 0

            #her opratter vi en array, der kan holde værdierne, som vi sætter ammen i en ny liste


            #så længe der satadig er flere elementer i leftlist og rightlist kør dette
            while len(leftlist) > leftI and len(rightlist) > rightI:
                #tjækker hvilke af listerne, der holder den laveste værdi
                if leftlist[leftI] < rightlist[rightI]:
                    #tilføjer leftlist[index] til tmp[tempI] i listen
                    listToSort[tempI] = leftlist[leftI]
                    #pludser 1 til leftI, så vi ikke tilføjer det samme igen.
                    leftI += 1
                else:
                    #det samme bare omvendt
                    listToSort[tempI] = rightlist[rightI]
                    rightI += 1

                #lægger 1 til tempI, så vi ikke overskriver det der lige er gemt
                tempI += 1

            #tjækker om der er flere elementer tilbage i hver af listerne, uden at være afhænig af hinanden.
            while len(rightlist) > rightI:
                listToSort[tempI] = rightlist[rightI]
                rightI+=1
                tempI+=1

            while len(leftlist) > leftI:
                listToSort[tempI] = leftlist[leftI]
                leftI+=1
                tempI+=1
            #retuneres tilbage til den forige funktion.
            return listToSort
        else:
            #er der kun et element i, retunere den bare listen tilbage.
            return listToSort

    #retuneres tilbage til dig martin <3 #NoHomoTho
    return mergeSortT(file.copy())



#       listen,  o til x, og hvor vi er
def heapIt(heap, size, index):

    #gemmer index, som den største
    largest = index

    #laver to childs
    leftHeap = 2 * index + 1
    rightHeap = 2 * index + 2

    #tjekker om vi er udenfor listens rækkevide, og om left child er højere en largest
    if leftHeap < size and heap[leftHeap] > heap[largest]:
        #gem left child, som largest
        largest = leftHeap

    #tjekker om vi er udenfor listens rækkevide, og om right child er højere en largest
    if rightHeap < size and heap[rightHeap] > heap[largest]:
        #gem right child, som largest
        largest = leftHeap

    #tjekker om vi har ændret på largest
    if largest != index:

        #byt rundt på den nye largest, og den gamle
        holder = heap[largest]
        heap[largest] = heap[index]
        heap[index] = holder

        #heapit
        heapIt(heap, size, largest)


def heapSort(file):
    #kopirer filen
    heap = file.copy()
    #find længden
    lenght = len(heap)

    #for alle elementer fra top til bund, kør heapit
    for i in range(lenght, -1, -1):
        heapIt(heap, lenght, i)

    #for alle elementer untagent aller sidst og først, swap med den første
    for n in range(lenght-1, 0, -1):

        holder = heap[n]
        heap[n] = heap[0]
        heap[0] = holder

        #og så heapit
        heapIt(heap, n, 0)

    #return den sorterede liste
    return heap



#min egen test
if __name__ == "__main__":
    listeja = [5,3,2,1,4]
    print(insertionSort(listeja))
    print(selectionSort(listeja))
    print(bubbleSort(listeja))
    print(mergeSort(listeja))
    print(heapSort(listeja))
