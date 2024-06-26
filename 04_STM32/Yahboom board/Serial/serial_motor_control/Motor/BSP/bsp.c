#include "bsp.h"

// LED显示当前运行状态，每10毫秒调用一次，LED灯每200毫秒闪烁一次。
// The LED displays the current operating status, which is invoked every 10 milliseconds, and the LED blinks every 200 milliseconds.  
extern UART_HandleTypeDef huart1;
extern uint8_t RxTemp;

static void Bsp_Led_Show_State_Handle(void)
{
	static uint8_t led_count = 0;
	led_count++;
	if (led_count > 20)
	{
		led_count = 0;
		LED_TOGGLE();
	}
}


// The peripheral device is initialized  外设设备初始化
void Bsp_Init(void)
{
	//Beep_On_Time(50);
	Motor_Init();
	USART1_Init();
}


// main.c中循环调用此函数，避免多次修改main.c文件。
// This function is called in a loop in main.c to avoid multiple modifications to the main.c file
void Bsp_Loop(void)
{
	// Detect button down events   检测按键按下事件
	HAL_UART_RxCpltCallback(&huart1);

	while(1){
		int speed = 0;

		if (RxTemp == '1')
		{
			speed = 2000;
			Motor_Set_Pwm(MOTOR_ID_M1, speed);
			Motor_Set_Pwm(MOTOR_ID_M2, speed);
			Motor_Set_Pwm(MOTOR_ID_M3, speed);
			Motor_Set_Pwm(MOTOR_ID_M4, speed);
		}
		if (RxTemp == '2')
		{
			// pause slowly
			Motor_Stop(0);
		}
		if (RxTemp == '3')
		{
			speed = -2000;
			Motor_Set_Pwm(MOTOR_ID_M1, speed);
			Motor_Set_Pwm(MOTOR_ID_M2, speed);
			Motor_Set_Pwm(MOTOR_ID_M3, speed);
			Motor_Set_Pwm(MOTOR_ID_M4, speed);
		}
		if (RxTemp == '4')
		{
			// immediately pause
			Motor_Stop(1);
		}
	}

	/*
	if (Key1_State(KEY_MODE_ONE_TIME))
	{
		//Beep_On_Time(50);

		static int state = 0;
		state++;
		int speed = 0;
	}*/

	//Bsp_Led_Show_State_Handle();
	//Beep_Timeout_Close_Handle();
	//HAL_Delay(10);
}
