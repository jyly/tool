;eg0415.asm
	include io32.inc
	.data
regd	byte 'EAX=',8 dup(0),'H',0
	.code
start:
	mov eax,1234abcdh
	xor ebx,ebx
	mov ecx,8	; 8位十六进制数
again:	rol eax,4
	push eax
	call htoasc	; 调用子程序
	mov regd+4[ebx],al
	pop eax
	inc ebx
	dec ecx
	jnz again
	mov eax,offset regd
	call dispmsg	; 显示

	exit 0
	; 子程序
htoasc	proc	; 过程定义，过程名为htoasc
	and al,0fh	; 只取AL的低4位
	or al,30h	; AL高4位变成3
	cmp al,39h	; 是0～9，还是A～F
	jbe htoend
	add al,7	; 是A～F，其ASCII码再加上7
htoend:	ret	; 子程序返回
htoasc	endp	; 过程结束
	
	end start