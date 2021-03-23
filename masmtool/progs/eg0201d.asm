; eg0201d.asm in MS-DOS
	include io16.inc
	.data
msg    byte 'ÄãºÃ£¬»ã±àÓïÑÔ!',13,10,0	;×Ö·û´®
	.code
start:
	mov ax,@data
	mov ds,ax
	mov eax,offset msg		;ÏÔÊ¾
	call dispmsg

	exit 0
	end start