;eg0202a.asm
	include io32.inc
	.data
count	dword 12345678h,9abcdef0h,0,0,3721h
	.code
start:
	mov eax,33221100h	; EAX=33221100H��������Ѱַ��
	mov ebx,eax		; EBX=EAX���Ĵ���Ѱַ��
	mov ecx,count		; ECX=12345678H��ֱ��Ѱַ��
	mov ebx,offset count	; EBX=count��������Ч��ַ��������Ѱַ��
	mov edx,[ebx]		; EDX=12345678H���Ĵ������Ѱַ��
	mov esi,[ebx+4]		; ESI=9ABCDEF0H���Ĵ������Ѱַ��
	mov esi,80000h		; ����������ָ����ַ��ʴ���
	mov count[esi],eax
	mov edi,count[esi]	; EDI=9ABCDEF0H���Ĵ������Ѱַ��
	mov edi,[ebx+esi]	; EDI=9ABCDEF0H����ַ��ַѰַ��
	mov ecx,[ebx+esi*4]	; ECX=3721H���������Ļ�ַ��ַѰַ��
	mov edx,[ebx+esi*4-4]	; EDX=0������������Ի�ַ��ַѰַ��
	mov ebp,esp		; EBP=ESP���Ĵ���Ѱַ��
	call disprd		; ��ʾ8��32λͨ�üĴ�������

	exit 0
	end start