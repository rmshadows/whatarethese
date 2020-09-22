package NekoFX;

import java.awt.AWTException;
import java.awt.MenuItem;
import java.awt.PopupMenu;
import java.awt.SystemTray;
import java.awt.TrayIcon;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URL;

import javax.swing.ImageIcon;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

/**
 * --module-path="c:\Program Files\Java\javafx-sdk-11.0.2\lib"
 * --add-modules=javafx.controls,javafx.fxml
 * 
 * @author Ryan
 *
 */

public class MainApp extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("/resources/Sample.fxml"));
			Scene scene = new Scene(root);
			scene.getStylesheets().add(getClass().getResource("/resources/application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.getIcons().add(new Image(MainApp.class.getResourceAsStream("/resources/title.png")));
			primaryStage.setTitle("Neko Manager");
			primaryStage.setResizable(false);
			Platform.setImplicitExit(false);//不会关闭程序
			primaryStage.setAlwaysOnTop(true);
			primaryStage.show();

			if (SystemTray.isSupported()) {
				try {
					URL resource = this.getClass().getResource("/resources/icon.png"); // 获得图片路径
					ImageIcon icon = new ImageIcon(resource); // 创建图片对象
					PopupMenu popupMenu = new PopupMenu(); // 创建弹出菜单对象
					MenuItem itemShow = new MenuItem("Main"); // 创建弹出菜单中的显示主窗体项.
					MenuItem itemExit = new MenuItem("Exit"); // 创建弹出菜单中的退出项
					TrayIcon trayIcon = new TrayIcon(icon.getImage(), "NekoM", popupMenu);
					trayIcon.setImageAutoSize(true);
					
					itemExit.addActionListener(new ActionListener() { // 给退出像添加事件监听
						@Override
						public void actionPerformed(ActionEvent e) {
							System.exit(0);
						}
					});
					
					itemShow.addActionListener(new ActionListener() { // 给窗体最小化添加事件监听.
						@Override
						public void actionPerformed(ActionEvent e) {
							
							Platform.runLater(new Runnable() {
						        @Override
						        public void run() {
						          primaryStage.show();//javaFX operations should go here
						        }
						   });
							trayIcon.displayMessage("Woops...", "来惹来惹 ~(=。=)~赏你个大红叉", TrayIcon.MessageType.ERROR);
						}
					});
					primaryStage.setOnCloseRequest(e->{
						trayIcon.displayMessage("提示", "缩小到系统托盘了哦~", TrayIcon.MessageType.INFO);
					});
					popupMenu.add(itemShow);
					popupMenu.add(itemExit);
					
					SystemTray sysTray = SystemTray.getSystemTray();
					try {
		                sysTray.add(trayIcon);
		            } catch (AWTException e1) {    
		            	
		            }
				} catch (Exception e) {
					System.out.println("系统托盘创建失败");
				}
			} else {
				System.out.println("系统托盘不支持");
			}
		}catch(	Exception e){
	            e.printStackTrace();
	    }
	}

	public static void main(String[] args) {
		launch(args);
	}
}
