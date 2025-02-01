# reverse number
def reverse_num(num):
    if num==0:
        return 0
    ulte_num=0
    negative_num=num<0
    num=abs(num)
    while num!=0:
        ulte_num=ulte_num*10+num%10
        num=num//10
    reversed_num=-ulte_num if negative_num else ulte_num
    return reversed_num
    
num=-23342
print(reverse_num(num))
#reverse a number using string method where u covert the int in str and then again in int
def reverse_n(num):
    if num<0:
        return -int(str(num)[:0:-1])
    else:
        return int(str(num)[::-1])
num=-1223
print(reverse_n(num))
# palindrom question leet code
class Solution(object):
    def isPalindrome(self, x):
        original_x=x
        reverse_num=0
        x=abs(x)
        while x!=0:
            reverse_num=reverse_num*10+x%10
            x=x//10
        if reverse_num==original_x:
            return True
        else:
            return False
#armstrong number qustion
def check_arm(num):
    real_num=num
    k=len(str(num))
    sum=0
    while num>0:
        ld=num%10
        sum+=ld**k
        num=num//10
    if sum==real_num:
        return "armstrong number"
    else:
        return"not armstrong number"
num=153
print(check_arm(num))
#wap to list out all the divisors of n number
def list_div(num):
    divisors=[]
    squareroot=num*2
    for i in range(1,squareroot+1):
        if num%i==0:
            divisors.append(i)
    return divisors
num=123
print(list_div(num))
#reverse the string
def sentence(s):
    p=s.lower()
    x="".join(p)
    return x
s="bOOBy, WHERE ARE U "
print(sentence(s))