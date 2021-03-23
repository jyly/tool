;eg0801.asm in DOS
	include io16.inc
	.data
freq	word 1193180/600	;给一个600Hz的频率
	.code
start:
	mov ax,@data
	mov ds,ax
	mov ax,freq
	call speaker	;设置扬声器的音调
	call speakon	;打开扬声器声音
	call readc	;等待按键

	call speakoff	;关闭扬声器声音
	exit 0
	;发音频率设置子程序，入口参数：AX＝1.19318×106÷发音频率
speaker	proc
	push ax	;暂存入口参数以免被破坏
	mov al,0b6h	;定时器2为方式3，先低后高写入16位计数值
	out 43h,al
	pop ax	;恢复入口参数
	out 42h,al	;写入低8位计数值
	mov al,ah
	out 42h,al	;写入高8位计数值
	ret
speaker	endp
speakon	proc	;扬声器开子程序
	push ax
	in al,61h	;读取61H端口的原控制信息
	or al,03h	;D1D0＝PB1PB0＝11，其他位不变
	out 61h,al	;直接控制发声
	pop ax
	ret
speakon	endp
speakoff	proc	;扬声器关子程序
	push ax
	in al,61h
	and al,0fch	;D1D0＝PB1PB0＝00，其他位不变 
	out 61h,al	;直接控制闭音
	pop ax
	ret
speakoff	endp

	end start
