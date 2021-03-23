include io32.inc
.data
	num  dword 3,1,4,5,2,6,-1,-2,-3,-4	;×Ö·û´®
	PLUS dword ?
.code
start:
	mov ecx,lengthof num
	xor eax,eax
	mov ebx,eax
	mov edx,eax
again:
	mov eax,num[ebx*(type num)]  ;Çå³ý¸ºÊý
	SHL eax,1
	jc rt
	SHR eax,1
	mov PLUS[edx*(type PLUS)],eax
	inc edx
rt:	
	inc ebx
	loop again
	push edx	
	xor eax,eax
	mov ebx,eax
	mov edx,eax 
outloop:	                    ;Ã°ÅÝÅÅÐò
	mov eax,PLUS[ebx*(type PLUS)]
	mov ecx,ebx
	inc ecx
inloop:
	cmp eax,PLUS[ecx*(type PLUS)]
	jc notbig
	xchg eax,PLUS[ecx*(type PLUS)]
	mov PLUS[ebx*(type PLUS)],eax
notbig:
	inc ecx
	cmp ecx,edx
	jng inloop
	inc ebx
	cmp ebx,edx
	jnge outloop
	pop edx
	xor eax,eax
	mov ebx,eax
done:
	mov eax,PLUS[ebx*(type PLUS)+(type PLUS)]		;ÏÔÊ¾
	call dispsid
	inc ebx
	cmp ebx,edx
	jc done
	exit 0
	end start

.data
	char byte ?
.code
start: 

	call readc
	cmp eax,'Z' 
	jc next
	sub eax,20H 

next:
	call dispc
	exit 0
	end start


	