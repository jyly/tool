;eg0403.asm
	include io32.inc
	.data
no_msg	byte 'Not Ready!',0
yes_msg	byte 'Ready to Go!',0
	.code
start:
	mov eax,56h	;����һ������
	test eax,02h	;����D1λ����10B��������߼���
	jz nom	;D1��0��ZF��1����ת�Ƶ�NOM
	mov eax,offset yes_msg
	jmp done	;������ת�ƣ�������һ����֧
nom:	mov eax,offset no_msg
done:	call dispmsg

	exit 0
	end start
