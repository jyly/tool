;eg0701.asm in DOS
	include io16.inc
	.data
msg	byte 'Hello, Assembly!',13,10,0		; ����Ҫ��ʾ���ַ���
	.code
start:	mov ax,@data
	mov ds,ax
	mov eax,offset msg	; ָ���ַ�����ƫ�Ƶ�ַ
	call dispmsg	; ����I/O�ӳ�����ʾ��Ϣ

	exit 0
	end start