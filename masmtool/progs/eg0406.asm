;eg0406.asm
	include io32.inc
	.data

	.code
start:
	call readsid	; ����һ���з���������EAX����ֵ
	cmp eax,0	; �Ƚ�EAX��0
	jge nonneg	; �������㣺AX��0��ת��
	neg eax	; ���������㣺AX��0��Ϊ���������󲹵���ֵ
nonneg:	call dispuid	; ��֧��������ʾ���

	exit 0
	end start
