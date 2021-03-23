;eg0415a.asm
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
	mov regd[ebx+4],al
	pop eax
	inc ebx
	dec ecx
	jnz again
	mov eax,offset regd
	call dispmsg	; 显示

	exit 0
	; 子程序
htoasc	proc	; 将AL低4位表达的一位十六进制数转换为ASCII码
	and eax,0fh	; 取得一位十六进制数
	mov al,ASCII[eax] 	; 换码	
	ret
	; 子程序的局部数据
ASCII	byte '0123456789ABCDEF'
htoasc	endp
	
	end start