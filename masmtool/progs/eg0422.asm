;eg0422.asm
	.686
	.model flat,stdcall
	option casemap:none
	includelib bin\kernel32.lib
ExitProcess	proto,:DWORD
exit	MACRO dwexitcode
	invoke ExitProcess,dwexitcode
	ENDM

GetStdHandle	proto,:DWORD
WriteConsoleA	proto,:DWORD,:DWORD,:DWORD,:DWORD,:DWORD
WriteConsole	equ <WriteConsoleA>
ReadConsoleA	proto,:DWORD,:DWORD,:DWORD,:DWORD,:DWORD
ReadConsole	equ <ReadConsoleA>
STD_INPUT_HANDLE	= -10
STD_OUTPUT_HANDLE	= -11

	.data
msg1	byte 'Please enter your name: ',0
msg2	byte 'Welcome ',0
nbuf	byte 80 dup(0)
msg3	byte ' to Win32 Console!',0

_outsize	dword ?
_outhandle	dword ?
_insize	dd ?
_inbuffer	byte 255 dup(0)

	.code
start:
	mov eax,offset msg1
	call dispmsg
	mov eax,offset nbuf
	call readmsg
	mov eax,offset msg2
	call dispmsg
	mov eax,offset nbuf
	call dispmsg
	mov eax,offset msg3
	call dispmsg
	
	exit 0

dispmsg	proc	; 字符串显示子程序，入口参数：EAX＝字符串地址
	push eax
	push ebx
	push ecx
	push edx
	push eax	; 保存入口参数，即字符串地址
	invoke GetStdHandle,STD_OUTPUT_HANDLE
	mov _outhandle,eax
	pop ebx	; EBX＝字符串地址
	xor ecx,ecx	; 计算字符串长度
dispm1:	mov al,[ebx+ecx]
	test al,al	
	jz dispm2
	inc ecx
	jmp dispm1
dispm2:	invoke WriteConsole,_outhandle,ebx,ecx,addr _outsize,0
	pop edx
	pop ecx
	pop ebx
	pop eax
	ret
dispmsg	endp

readmsg	proc	; 字符串输入子程序，入口参数：EAX＝缓冲区地址
	push ebx
	push ecx
	push edx
	push eax	; 保护输入的缓冲区地址参数
	invoke GetStdHandle,STD_INPUT_HANDLE
	invoke ReadConsole,eax,addr _inbuffer,255,addr _insize, 0
	sub _insize,2
	xor ecx,ecx
	pop ebx	; 获得缓冲区地址
readm1:	mov al,_inbuffer[ecx]
	mov [ebx+ecx],al	; 将输入的字符串复制到用户缓冲区
	inc ecx
	cmp ecx,_insize
	jb readm1
	mov byte ptr [ebx+ecx],0	; 最后填入结尾字符0
	mov eax,ecx
	pop edx
	pop ecx
	pop ebx
	ret
readmsg	endp

	end start
