import java.util.Scanner;

public class UpsideDownLetters {
	//所需数组、特殊符号以及程序状态控制变量
	private static String[] r = new String[]{"ɐ","q","ɔ","p","ǝ","ɟ","ɓ","ɥ","!","ſ̣","ʞ","ן","ɯ","u","o","d","b","ɹ","s","ʇ","n","ʌ","ʍ","x","ʎ","z"};
	private static String[] R = new String[]{"ꓯ","ꓭ","ꓛ","ꓷ","ꓱ","ꓞ","ꓨ","H","I","ꓩ","ꓘ","ꓶ","W","N","O","ꓒ","σ","ꓤ","S","ꓕ","ꓵ","ꓥ","ꓟ","X","⅄","Z"};
	private static String symbol = " ꦿ";
	private static int status;
	private static String result = "";
	private static String text="";
	//打印程序信息
	private static void info() {
		System.out.println("--------------------------------");
		System.out.println("-----------#########------------");
		System.out.println("-----------###-----##-----------");
		System.out.println("-----------###-----##-----------");
		System.out.println("-----------########-------------");
		System.out.println("-----------###---###------------");
		System.out.println("-----------###-----###----------");
		System.out.println("--------------------------------");
		System.out.println("DESIGNED BY R.M.Y. \n2019/08/10");
		System.out.println("--------------------------------\n");
	}
	//正常模式
	@SuppressWarnings("resource")
	private static void upsideDown() {
		do {text=result="";
			System.out.println("-------------------------------------------");
			System.out.println("请输入需要倒置的文字(仅允许大小写英文字母)：\n\n99)返回上级菜单");
			System.out.println("-------------------------------------------\n");
			Scanner s = new Scanner(System.in);
			text = s.next();
			StringBuffer buffer = new StringBuffer(text);//倒序字符串buffer.reverse()
//			return;
//			if(text=="99") {
//				return;
//			}
			String re = buffer.reverse().toString();//re为顺序相反的字符串
			for(int i=0;i<buffer.toString().length();i++) {
				int num;
				num = re.charAt(i);
				if(num==57) {//数字9结束当前方法
					return;
				}
				else if(num==32) {//空格
					result += " ";
				}
				else if(num>64 && num<91) {//a:97-122 A:65-90
					result += R[num-65];
				}
				else if (num<123 && num>96) {
					result += r[num-97];
				}
				else {
					System.out.println("请检查输入！");
					break;
				}
			}
			System.out.println("颠倒后的结果："+result);
			buffer = new StringBuffer();
			result = "";
			text = "";//清零
		}while(text!="99");
	}
	//花里胡哨模式
	@SuppressWarnings("resource")
	private static void whistling() {
		do {System.out.println("----------------------------------------------");
			System.out.println("当前处于花里胡哨模式，请输入文字(支持所有文字)：\n99)返回上级菜单\n");
			System.out.println("----------------------------------------------\n");
			text=result="";
			Scanner s = new Scanner(System.in);
			text = s.next();
			for(int i=0;i<text.length();i++) {
				if(text.charAt(0)=='9'&&text.length()==1) {
					System.out.println("9"+symbol);
				}
				else if(text.charAt(0)=='9'&&text.charAt(1)=='9'&&text.length()==2) {
					System.out.println("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%");
					System.out.println("是否返回上级菜单？(除‘Y’外任意键字符继续，输入‘Y’确认返回)");
					System.out.println("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n");
					Scanner b = new Scanner(System.in);
					String t = b.next();
					if(t.length()==1 && (t.charAt(0)=='y' || t.charAt(0)=='Y')) {
						return;
					}
					else {
						System.out.println("9 ꦿ9 ꦿ");
					}
				}
				else {
					result += text.charAt(i);
					result += symbol;
				}
			}
			System.out.println(result);
		}while(text!="99");
	}
	//程序头部
	private static void header() {
		do {System.out.println("------------------------------");
			System.out.println("欢迎使用本程序，请选择工作模式！");
			System.out.println("1)字母颠倒模式\n2)花里胡哨模式\n3)程序信息\n\n99)退出程序");
			System.out.println("------------------------------");
			@SuppressWarnings("resource")
			Scanner choose = new Scanner(System.in);
			String c = choose.next();//1,2,3,9-49,50,51,57		
			if((c.length()==1&&(c.charAt(0)==49||c.charAt(0)==50||c.charAt(0)==51))||(c.length()==2&&c.charAt(0)==57&&c.charAt(1)==57)) {
				status = Integer.parseInt(c);
				switch (status) {
					case 1:
						upsideDown();
						break;
					case 2:
						whistling();
						break;
					case 3:
						info();
						break;
					case 99:
						System.out.println("\n\n正在退出......\n\n");
						break;
					default:
						System.out.println("请输入数字1~3或99");
						break;
				}
			}
			else {
				System.out.println("请重新输入指定选项！");
			}
		}while(status!=99);
		System.out.println("感谢使用！");
		return;
	}
	//程序入口
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		header();
	}

}