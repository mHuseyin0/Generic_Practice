.data
	message: .asciiz "This is message \n"
	character: .byte '$'
	space: .asciiz " "
	newline: .asciiz "\n"
	dashes: .asciiz "-----------------------------------"
	integer: .word 45
	addInteger: .word 1
	float: .float 4.213
	zeroFloat: .float 0.0
	double: .double 5.444
	zeroDouble: .double 0.0
	prompt: .asciiz "Please enter a number: "
	namePrompt: .asciiz "Please enter your name: "
	textInput: .space 20 # 20 characters long text
	# .space reserves 20 bytes in the memory
.text
	main:
	li $v0, 4
	la $a0, message
	syscall
	
	li $v0, 4
	la $a0, character
	syscall
	
	li $v0, 1
	lw $a0, integer
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	
	li $v0, 2
	lwc1 $f12, float
	syscall

	li $v0, 4
	la $a0, newline
	syscall
	
	# If we want to work with floats or doubles, we have to load them into coprocessor 1
	# ldc1 for doubles and ldf1 for floats
	# odd indexes in cp1 shouldn't be manipulated directly since they store the continuing decimals of the number
	# in the index before them
	# Also add.d for doubles and add.s for floats must be used instead of add
	# Similarly there are sub.s, sub.d, mul.s, mul.d, div.s, div.d

	ldc1 $f0, zeroDouble # doubles uses 2 registers, so difference between two consecutive double registers should be even 
	ldc1 $f2, double
	li $v0, 3
	add.d $f12, $f2, $f0
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	
	lw $t0, integer($zero)
	lw $t1, addInteger($zero)
	add $t2, $t0, $t1
	li $v0, 1
	add $a0, $zero, $t2
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	
	sub $t2, $t1, $t0
	li $v0, 1
	move $a0, $t2
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	
	addi $t3, $zero, 10
	addi $t4, $zero, 6
	mul $t5, $t3, $t4
	li $v0, 1
	add $a0, $zero, $t5
	syscall

	li $v0, 4
	la $a0, newline
	syscall
	
	mult $t3, $t0 # Allows us to multiply larger numbers. Product is stored in 2 registers called lo and hi
	mflo $t5
	li $v0, 1
	add $a0, $zero, $t5
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	
	sll $t5, $t0, 1
	li $v0, 1
	add $a0, $zero, $t5
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	
	div $t5, $t0, $t3 # 45 divided by 10 prints 4
	li $v0, 1
	add $a0, $zero, $t5
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	
	div $t0, $t3 # With two arguments, stores quotient and remainder in lo and hi
	li $v0, 1
	mflo $t5
	add $a0, $zero, $t5
	syscall

	li $v0, 4
	la $a0, space
	syscall
	
	li $v0, 1
	mfhi $t5
	add $a0, $zero, $t5
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	
	jal printDash
	
	addi $s0, $zero, 10
	
	jal printPlusFive
	jal printNewline
	
	# s0 does not change in main
	li $v0, 1
	move $a0, $s0
	syscall
	
	jal printNewline
	
	addi $t0, $zero, 60
	
	# t0 will change here
	jal addFive
	
	li $v0, 1
	move $a0, $t0
	syscall
	
	# You don't have to save t registers to stack in functiona. Procedures have permission to change them unlike s registers
	
	jal printNewline
	la $s0, prompt
	jal prints0text 
	
	lwc1 $f4, zeroFloat
	
	# 5 to take integer, 6 to take float, 7 to take double
	li $v0, 6
	syscall
	
	# In case of float and double, v0 implicitly goes to f0
	
	# Store the input in another register to use v0
	#move $s0, $v0
	li $v0, 2
	add.s $f12, $f4, $f0
	syscall
	
	jal printNewline
	la $s0, namePrompt
	jal prints0text
	
	li $v0, 8
	la $a0, textInput
	li $a1, 20
	syscall
	
	la $t0, textInput
	jal printt0text
	
	# Tell the system the program is done. (Use if you have procedures)
	li $v0, 10
	syscall
	
	printNewline:
		li $v0, 4
		la $a0, newline
		syscall
		
		jr $ra
		
	printDash:
		li $v0, 4
		la $a0, dashes
		syscall
		
		addi $sp, $sp, -4 # In order to use nested procedures
		sw $ra, 0($sp)
		
		jal printNewline
		
		lw $ra, 0($sp)
		addi $sp, $sp, 4
		
		
		jr $ra # Jump to place where this was called
			
	printPlusFive:
		addi $sp, $sp, -4 # Allocate 4 bytes in stack
		sw $s0, 0($sp) # Store s0 at 0 location
			
		addi $s0, $s0, 5
		
		li $v0, 1
		move $a0, $s0
		syscall
	
		lw $s0, 0($sp) # Restore the value of s0
		addi $sp, $sp, 4 # Free the memory
	
		li $v0, 1
		move $a0, $s0
		syscall
	
			
		jr $ra
		
	addFive:
		addi $t0, $t0, 5
		jr $ra
	prints0text:
		li $v0, 4
		move $a0, $s0
		syscall
		jr $ra
	printt0text:
		li $v0, 4
		move $a0, $t0
		syscall
		jr $ra
	prints0int:
		li $v0, 1
		move $a0, $s0
		syscall
		jr $ra
	printt0int:
		li $v0, 1
		move $a0, $t0
		syscall
		jr $ra
