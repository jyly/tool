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
szCaption	byte '消息窗口',0
outbuffer	byte '本机的处理器是', 12 dup(0),0
outbufsize	= sizeof outbuffer-1
	.code
start:
	mov eax,0
	cpuid	; 执行处理器识别指令
	mov dword ptr outbuffer+outbufsize-12,ebx
	mov dword ptr outbuffer+outbufsize-8,edx
	mov dword ptr outbuffer+outbufsize-4,ecx
	invoke MessageBox,NULL,addr outbuffer, addr szCaption,MB_OK
	invoke ExitProcess,NULL
	end start
