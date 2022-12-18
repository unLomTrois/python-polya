"""
    �������� ��������� ������������ �������� ���, ����� ����� ����� ����� ���� ������ � ����������.

    def TumbaWords(A, w, L):
    if len(w) == L:
        print(w)
        return;

    for c in A:
        TumbaWords(A, w+c, L)
"""

"""
    ����������� ���������� ���� ��������� ����� �� ���������� ��������, ���:
    - A - �������(������ ��������)
    - w - ����� ��� ������(� ��� ��� � ������������)
    - L - ������ �����
"""


def TumbaWords(A, w, L):
    if len(w) == L:
        print(w)
        return

    for c in A:
        TumbaWords(A, w + c, L)


l = int(input("enter length: "))
A = ["�", "�", "�", "�"]
TumbaWords(A, "", l)
