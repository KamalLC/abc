
class Node:
	def __init__(self, value=None, next=None):
		self.value=value
		self.next=next


class LinkedList:
	def __init__(self):
		self.head=None

	def insertAtFirst(self, value):
		newNode=Node(value, self.head)
		self.head=newNode

	def insertAtLast(self, value):
		newNode=Node(value)

		traverse=self.head
		while(traverse.next):
			traverse=traverse.next
		traverse.next=newNode

	def insertAt(self, value, index):
		traverse=self.head
		count=0
		if(index==0):
			self.insertAtFirst(value)
			return
		if(traverse is None and index != 0):
			print("index out of range")
			return

		while(traverse.next and count<index-1):
			count+=1
			traverse=traverse.next
		if(count==index-1):
			newNode=Node(value,traverse.next)
			traverse.next=newNode
		else:
			print("index out of range")

	def clear(self):
		self.head=None

	def removeFirst(self):
		traverse=self.head
		if(traverse is None):
			print("empty linked list")
		else:
			temp=self.head.value
			self.head=traverse.next
			return temp


	def removeLast(self):
		traverse=self.head
		if(traverse is None):
			print("empty linked list")
			return
		while(traverse.next.next):
			traverse=traverse.next
		temp=traverse.next.value
		traverse.next=None
		return temp

	def removeAt(self, index):
		traverse=self.head
		count=0
		if(index==0):
			self.removeFirst()

		while(traverse and index-1 != count):
			count+=1
			traverse=traverse.next

		if(count==index-1):
			temp=traverst.next.next.value
			traverse.next=traverse.next.next
			return temp
		else:
			print("index out of range")


	def printL(self):
		curr=self.head
		display=""

		if(curr is None):
			print("linked list is empty")
			return

		while(curr):
			display+=str(curr.value)+"-->"
			curr=curr.next
		print(display)

# if __name__ == '__main__':
# ll=LinkedList()
# ll.insertAtFirst(2)
# ll.insertAtFirst(4)
# ll.insertAtFirst(6)
# ll.insertAtLast(10)
# ll.insertAt(5, 3)
# # ll.removeFirst()
# ll.removeAt(0)

# ll.printL()

# ll.clear()
# ll.printL()