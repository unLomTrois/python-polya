
'''
    3. � ����� � ������� �������� ����� �����. �������� ���������, ������� ���������� ����� 
    ����� ������� ������� ������ ������ ���������� ����� � ������� ��������� � ������ ����. 

'''

path = 'D:/�������/4 ����/�������� - ��/��������/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name = 'input.txt', 'output.txt';

nums = [];
for numS in open(path + txt1name):
    nums.append(int(numS))

# ������ ���������� ��������
maxCount, count = 1, 1; # maxCount - ������������ ���-��, count - ������� ���-��
for i in range(1,len(nums)):
    if nums[i-1] == nums[i]:
        count += 1;
    else:
        if count >= maxCount:
            maxCount = count;
        count = 1;
if count > maxCount:
    maxCount = count;
# ����� ���������� ��������

with open(path + txt2name, 'w') as f:
    f.write('length = {:}\n'.format(maxCount));