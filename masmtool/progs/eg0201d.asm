; eg0201d.asm in MS-DOS
	include io16.inc
	.data
msg    byte '��ã��������!',13,10,0	;�ַ���
	.code
start:
	mov ax,@data
	mov ds,ax
	mov eax,offset msg		;��ʾ
	call dispmsg

	exit 0
	end start