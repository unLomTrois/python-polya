
'''
    5. � ����� �������� � ������� ����� �����. ������������� �� �� ����������� ����� ���� � �������� � ������ ����.
'''

# ���������� ����� ���� ����������� �����
def get_sum_digits(num):
    s = 0;
    for symbol in str(num):
        s += int(symbol)
    return s;


path = 'D:/�������/4 ����/�������� - ��/��������/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name = 'input.txt', 'output.txt';

nums = [];
for numS in open(path + txt1name):
    nums.append(int(numS))

# ������ ���������� ��������
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if get_sum_digits(nums[i]) > get_sum_digits(nums[j]):
            nums[i], nums[j] = nums[j], nums[i];
    
# ����� ���������� ��������

with open(path + txt2name, 'w') as f:
    for num in nums:
        f.write('{:}\n'.format(num));