;eg0705.asm in DOS
	include io16.inc
	.data
intoff	word ?	;用于保存原中断服务程序的偏移地址
intseg	word ? 	;用于保存原中断服务程序的段地址
intmsg	byte 'A Instruction Interrupt !',0dh,0ah,0	;字符串（以0结尾）
	.code
start:
	mov ax,@data
	mov ds,ax
	mov ax,3580h	;获取系统的原80H中断向量
	int 21h
	mov intoff,bx	;保存偏移地址
	mov intseg,es	;保存段基地址
	push ds
	mov dx,offset new80h
	mov ax,seg new80h
	mov ds,ax
	mov ax,2580h	;设置本程序的80H中断向量
	int 21h
	pop ds
	;
	mov dx,offset intmsg	;设置入口参数DS和DX
	int 80h	;调用80H中断服务程序，显示字符串
	;
	mov dx,intoff	;恢复系统的原80H中断向量
	mov ax,intseg	;注意先设置DX、后设置DS入口参数
	mov ds,ax	;因为先改变了DS，就不能准确取得intoff变量值
	mov ax,2580h
	int 21h
	exit 0

	;80H内部中断服务程序：显示字符串（以0结尾）；DS∶DX＝缓冲区首地址
new80h	proc	;过程定义
	sti	;开中断
	push ax	;保护寄存器
	push bx
	push si
	mov si,dx
new1:	mov al,[si]	;获取欲显示字符
	cmp al,0	;为“0”结束
	jz new2
	mov bx,0	;采用ROM-BIOS调用显示一个字符
	mov ah,0eh
	int 10h
	inc si	;显示下一个字符
	jmp new1
new2:	pop si	;恢复寄存器
	pop bx
	pop ax
	iret	;中断返回
new80h	endp	;中断服务程序结束

	end start
