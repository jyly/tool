; eg0201b.asm in Windows Console
	include io32.inc
	.data
msg    byte '��ã�������ԣ�',13,10,0	;�ַ���
	.code
start:
	mov eax,offset msg		;��ʾ
	call dispmsg

	exit 0
	end start