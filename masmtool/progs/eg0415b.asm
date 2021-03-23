;eg0415b.asm
	include io32.inc
	.data
regd	byte 'EAX=',8 dup(0),'H',0
	.code
start:
	mov eax,1234abcdh
	mov ebx,4
	mov ecx,8	; 8位十六进制数
again:	rol eax,4
	push eax
	call htoasc	; 调用子程序
	mov regd[ebx],al
	pop eax
	inc ebx
	dec ecx
	jnz again
	mov eax,offset regd
	call dispmsg	; 显示

	exit 0
	; 子程序
htoasc	proc	; 将AL低4位表达的一位十六进制数转换为ASCII码
	push ebx
	mov ebx,offset ASCII 
	and al,0fh	; 取得一位十六进制数
	xlat ASCII	; 换码：AL←CS:[EBX＋AL]，注意数据在代码段CS
	pop ebx
	ret
	; 子程序的局部数据
ASCII	byte '0123456789ABCDEF'
htoasc	endp
	
	end start