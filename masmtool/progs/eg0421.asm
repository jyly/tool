;eg0421.asm
	.686
	.model flat,stdcall
	option casemap:none
	includelib bin\kernel32.lib
ExitProcess	proto,:DWORD
GetStdHandle	proto,:DWORD
WriteConsoleA	proto,:DWORD,:DWORD,:DWORD,:DWORD,:DWORD
WriteConsole	equ <WriteConsoleA>
STD_OUTPUT_HANDLE	= -11
	.data
outhandle	dword ?
outbuffer	byte 'The processor vendor ID is ', 12 dup(0)
outbufsize	= sizeof outbuffer
outsize	dd ?
	.code
start:
	mov eax,0
	cpuid	; ִ�д�����ʶ��ָ��
	mov dword ptr outbuffer+outbufsize-12,ebx
	mov dword ptr outbuffer+outbufsize-8,edx
	mov dword ptr outbuffer+outbufsize-4,ecx
	; ���������
	invoke GetStdHandle,STD_OUTPUT_HANDLE
	mov outhandle,eax
	; ��ʾ��Ϣ
	invoke WriteConsole,outhandle,addr outbuffer,outbufsize,addr outsize,0
	; �˳�
	invoke ExitProcess,0
	end start
