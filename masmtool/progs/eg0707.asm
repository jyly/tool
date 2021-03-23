;eg0707.asm in DOS
	include io16.inc
	.code
new04h	proc	;中断服务程序
	sti
	push ax	;保存寄存器
	push bx
	push si
	push ds
	mov ax,cs	;数据在代码段中，故DS＝CS
	mov ds,ax
	mov si,offset intmsg
dps1:	mov al,[si]
	cmp al,0
	jz dps2
	mov bx,0	;调用ROM-BIOS功能显示al中的字符
	mov ah,0eh
	int 10h
	inc si
	jmp dps1
dps2:	pop ds	;恢复寄存器
	pop si
	pop bx
	pop ax
	iret	;中断返回
intmsg  byte 0dh,0ah,'Overflow !',0
new04h	endp	;中断服务程序结束
	;主程序开始
start:	mov ax,cs
	mov ds,ax	;设置04H中断向量	
	mov dx,offset new04h
	cli
	mov ax,2504h
	int 21h
	sti
	mov ax,offset tsrmsg	;显示安装信息
	call dispmsg
	mov dx,offset start	;计算驻留内存程序的长度
	add dx,256+15
	shr dx,4	;调整为以“节”（16个字节）为单位
	mov ax,3100h	;程序驻留，返回DOS	
	int 21h
tsrmsg	byte 'INT 04H Program Installed !',0dh,0ah,0
	end start
