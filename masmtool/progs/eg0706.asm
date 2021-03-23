;eg0706.asm in DOS
	include io16.inc
	.data
intmsg	byte  'A 8259A Interrupt !',0dh,0ah,0
counter	byte 0	;中断次数记录单元
	.code
start:
	mov ax,@data
	mov ds,ax
	mov ax,3508h	;获取原中断向量
	int 21h
	push es	;保存原中断向量（利用堆栈）
	push bx
	cli	;关中断
	push ds	;设置新中断向量 
	mov ax,seg new08h
	mov ds,ax
	mov dx,offset new08h
	mov ax,2508h
	int 21h
	pop ds
	in al,21h	;读出IMR
	push ax	;保存原IMR内容
	and al,0feh	;允许IRQ0，其他不变
	out 21h,al	;设置新IMR内容	
	mov counter,0	;设置中断次数初值
	sti	;开中断
	;主程序完成中断服务程序设置，可以处理其他事务
start1:	cmp counter,10	;本例的主程序仅循环等待中断
	jb start1	;中断10次退出
	;
	cli	;关中断
	pop ax	;恢复IMR
	out 21h,al
	pop dx	;恢复原中断向量
	pop ds
	mov ax,2508h
	int 21h
	sti	;开中断
	exit 0

	; 中断服务程序
new08h	proc 
	sti	;开中断
	push ax	;保护寄存器
	push si
	push ds
	mov ax,@data	;外部随机产生中断，DS也不确定，所以必须设置DS
	mov ds,ax
	inc counter	;中断次数加1
	mov si,offset intmsg	;显示信息
	call dpstri 
	mov al,20h	;发送EOI命令
	out 20h,al
	pop ds	;恢复寄存器
	pop si
	pop ax
	iret	;中断返回
new08h	endp
dpstri	proc	;显示字符串子程序
	push ax	;入口参数：DS:SI＝字符串首址
	push bx
dps1:	mov al,[si]
	cmp al,0
	jz dps2
	mov bx,0	;调用ROM-BIOS功能显示al中的字符
	mov ah,0eh
	int 10h
	inc si
	jmp dps1
dps2:	pop bx
	pop ax
	ret
dpstri	endp

	end start
