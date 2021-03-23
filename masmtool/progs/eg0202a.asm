;eg0202a.asm
	include io32.inc
	.data
count	dword 12345678h,9abcdef0h,0,0,3721h
	.code
start:
	mov eax,33221100h	; EAX=33221100H（立即数寻址）
	mov ebx,eax		; EBX=EAX（寄存器寻址）
	mov ecx,count		; ECX=12345678H（直接寻址）
	mov ebx,offset count	; EBX=count变量的有效地址（立即数寻址）
	mov edx,[ebx]		; EDX=12345678H（寄存器间接寻址）
	mov esi,[ebx+4]		; ESI=9ABCDEF0H（寄存器相对寻址）
	mov esi,80000h		; 将引起下条指令出现访问错误
	mov count[esi],eax
	mov edi,count[esi]	; EDI=9ABCDEF0H（寄存器相对寻址）
	mov edi,[ebx+esi]	; EDI=9ABCDEF0H（基址变址寻址）
	mov ecx,[ebx+esi*4]	; ECX=3721H（带比例的基址变址寻址）
	mov edx,[ebx+esi*4-4]	; EDX=0（带比例的相对基址变址寻址）
	mov ebp,esp		; EBP=ESP（寄存器寻址）
	call disprd		; 显示8个32位通用寄存器内容

	exit 0
	end start