;eg0404.asm
	include io32.inc
	.data

	.code
start:
	call readc	; �������룬����ֵ��AL�Ĵ���
	call dispcrlf	; �س����У����ڷָ���
	call dispbb	; �Զ�������ʽ��ʾ����
	call dispcrlf	; �س����У����ڷָ���
	and al,7fh	; ���λ��"0"������λ���䣬ͬʱ��־PF��ӳ"1"�ĸ���
	jnp next	; ����Ϊ���������账��ת��
	or al,80h	; ����Ϊż�������λ��"1"������λ���� 
next:	call dispbb	; ��ʾ��У��λ������

	exit 0
	end start
