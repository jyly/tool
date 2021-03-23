;eg0701.asm in DOS
	include io16.inc
	.data
msg	byte 'Hello, Assembly!',13,10,0		; 定义要显示的字符串
	.code
start:	mov ax,@data
	mov ds,ax
	mov eax,offset msg	; 指定字符串的偏移地址
	call dispmsg	; 调用I/O子程序显示信息

	exit 0
	end start