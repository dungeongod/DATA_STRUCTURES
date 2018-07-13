class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
class LL:
	def __init__(self):
		self.head = None
	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next
	

		

if __name__ == '__main__':
	llist = LL()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	llist.head.next = second
	second.next = third

	newNode = Node(4)
	newNode.next = llist.head
	llist.head = newNode

	helloNode = Node(5)
	helloNode.next = llist.head
	llist.head = helloNode
	
	
llist.printlist()

