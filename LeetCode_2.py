'''
import chaintable as ct
	
l1 = ct.ChainTable()
l1.append(2)	
l1.append(4)	
l1.append(3)
	
l2 = ct.ChainTable()	
l2.append(5)	
l2.append(6)	
l2.append(4)	

l1.show()
l2.show()

number1 = 0
timee = 1
node = l1.head
while node:
	number1 += node.data*timee
	node = node._next
	timee = timee * 10
print(number1)	

number2 = 0
timee = 1
node =l2.head
while node:
	number2 += node.data*timee
	node = node._next
	timee = timee *10
print(number2)
	
number3 = number1 + number2
print(number3)

re = ct.ChainTable()
while(number3):
	re.append(number3%10)
	number3//=10
re.show()
'''
'''
while number3 > 0:
	re.append(result,int(str(number3)[-1]))
	number3 = (number3 - int(str(number3)[-1])/10
	
re.show()	'''	
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
		number1 = 0
		time = 1
		node = l1
		while node:
			number1 += node.val * time
			node = node.next
			time = time * 10

		number2 = 0
		time = 1
		node = l2
		while node:
			number2 += node.val *time
			node = node.next
			time = time * 10

		number3 = number1 + number2
		dummyRoot = ListNode(0)
		re = dummyRoot
		while(number3):
			re.next = ListNode(number3%10)
			number3//=10
			re=re.next
		re = dummyRoot.next
		return re
		
		
		
def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
	numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
		
		
		
		
		
		
		
		