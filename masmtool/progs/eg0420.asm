;eg0420.asm（主程序文件）
	include io32.inc
	extern read:near,write:near,mean:near	; 外部子程序
	public temp	; 变量共用
	.data
count	= 10
array	dword count dup(0)
temp	dword ?
msg1	byte 'Enter 10 numbers: ',13,10,0
msg2	byte 'The mean is: ',0
	.code
start:
	mov eax,offset msg1	; 提示输入10个数据
	call dispmsg
	xor ebx,ebx 
	mov ecx,count	; ECX＝数据个数
again:	call read	; 调用子程序，输入一个数据
	mov eax,temp	; 获得出口参数
	mov array [ebx*4],eax 
	add ebx,1
	cmp ebx,count
	jb again
	push ecx	; 传递参数
	push offset array
	call mean	; 调用子程序，求平均值
	add esp,8
	mov ebx,eax	; EAX返回值转存到EBX
	mov eax,offset msg2	; 提示输出平均值
	call dispmsg 
	mov eax,ebx	; 提示输出平均值
	call write	; 调用子程序，显示平均值
	exit 0
	end start
