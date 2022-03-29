from linked_list import LinkedList
import pytest

def test_get_element():
    
    linked_list = LinkedList()

    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')

    assert linked_list.get_element(0) == 'c'
    assert linked_list.get_element(1) == 'b'
    assert linked_list.get_element(2) == 'a'

def test_count():
    
    linked_list = LinkedList()

    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')

    assert linked_list.count()==3

def test_pop_front():
    linked_list = LinkedList()
    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')
    assert linked_list.pop_front()=='c'
    assert linked_list.count()==2
    assert linked_list.pop_front()=='b'
    assert linked_list.count()==1
    

def test_insert_after():
    linked_list = LinkedList()
    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')
    linked_list.insert_after(1,'d')
    assert linked_list.count() == 4
    assert linked_list.get_element(0) == 'c'
    assert linked_list.get_element(1) == 'b'
    assert linked_list.get_element(2) == 'd'
    assert linked_list.get_element(3) == 'a'


def test_remove_element():
    linked_list = LinkedList()
    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')
    linked_list.push_front('d')
    assert linked_list.remove_element(2) == 'b'
    assert linked_list.get_element(2) == 'a'

def test_reverse():
    linked_list = LinkedList()
    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')
    linked_list.push_front('d')
    linked_list.reverse()
    assert linked_list.get_element(0)== 'a'
    assert linked_list.get_element(1)== 'b'
    assert linked_list.get_element(2)== 'c'
    assert linked_list.get_element(3)== 'd'