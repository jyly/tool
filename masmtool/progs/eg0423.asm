;eg0423.asm
	.686
	.model flat,stdcall
	option casemap:none
	includelib bin\kernel32.lib
	includelib bin\user32.lib
ExitProcess	proto,:DWORD
MessageBoxA PROTO :DWORD,:DWORD,:DWORD,:DWORD
MessageBox equ <MessageBoxA>
NULL	equ 0
MB_OK	equ 0
	.data
szCaption	byte '��Ϣ����',0
outbuffer	byte '�����Ĵ�������', 12 dup(0),0
outbufsize	= sizeof outbuffer-1
	.code
start:
	mov eax,0
	cpuid	; ִ�д�����ʶ��ָ��
	mov dword ptr outbuffer+outbufsize-12,ebx
	mov dword ptr outbuffer+outbufsize-8,edx
	mov dword ptr outbuffer+outbufsize-4,ecx
	invoke MessageBox,NULL,addr outbuffer, addr szCaption,MB_OK
	invoke ExitProcess,NULL
	end start
