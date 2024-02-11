package Neko11;

import java.awt.GraphicsConfiguration;
import java.awt.Insets;
import java.awt.MouseInfo;
import java.awt.Point;
import java.awt.PointerInfo;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.Timer;

/**
 * Neko the cat.
 * 下面代码不是我写的！！作者是：Werner Randelshofer 。具体参见README.md谢谢！！
 * <p>
 * This program loads in 32 images of Neko, and tests them. (to show you that
 * they've been loaded). Neko will chase you mouse cursor around the desktop.
 * Once she's over it and the mouse doesn't move she'll prepare to take a nap.
 * If the mouse go's outside the desktop she will reach the border and try to
 * dig for it. She'll eventually give up, and fall asleep.
 *
 *
 * @author Werner Randelshofer (adaption for desktop) Chris Parent (original
 *         code)
 * @version 1.0.1 2010-07-17 Fixes timers. Sets longer sleep times when the cat
 *          sleeps. <br>
 *          1.0 2010-07-16 Created.
 */
public class NekoM11 extends javax.swing.JWindow {
	// Constants

	private final double pi = Math.PI;
	private final int over = 1;
	private final int under = 2;
	private final int left = 3;
	private final int right = 4;

	// Variables
	private int pos; // neko's position
	private int x, y; // mouse pos.
	private int ox, oy; // image pos.
	private int dx, dy; // image-mouse distance
	private int no; // image number.
	private int init; // for image loading initialize counter
	private int slp; // sleep time
	private int ilc1; // image loop counter
	private int ilc2; // second loop counter
	private boolean move; // mouse move, flag
	private boolean out; // mouse exiseted, flag
	private double theta; // image-mouse polar data
	private double dist; // distance
	private ImageIcon image[]; // images
	private Point windowOffset = new Point(-16, -30);
	private Rectangle nekoBounds = new Rectangle();
	private Timer timer;

	/** Creates new form Neko */
	public NekoM11() {

		getRootPane().putClientProperty("Window.shadow", false);

		setAlwaysOnTop(true);

		initComponents();
		loadKitten();
		imageLabel.setSize(100, 100);

		setSize(image[1].getIconWidth(), image[1].getIconHeight());
		setLocation(ox + windowOffset.x, oy + windowOffset.y);

		timer = new Timer(200, new ActionListener() {

			public void actionPerformed(ActionEvent e) {
				locateMouseAndAnimateCat();
			}
		});
		timer.setRepeats(true);
		timer.start();
	}

	/**
	 * This method is called from within the constructor to initialize the form.
	 * WARNING: Do NOT modify this code. The content of this method is always
	 * regenerated by the Form Editor.
	 */
	@SuppressWarnings("unchecked")
	// <editor-fold defaultstate="collapsed" desc="Generated
	// Code">//GEN-BEGIN:initComponents
	private void initComponents() {

		imageLabel = new javax.swing.JLabel();
//		imageLabel.setSize(100, 100);

		FormListener formListener = new FormListener();

		imageLabel.addMouseListener(formListener);
		getContentPane().add(imageLabel, java.awt.BorderLayout.CENTER);

		pack();
	}

	// Code for dispatching events from components to event handlers.

	private class FormListener implements java.awt.event.MouseListener {
		FormListener() {
		}

		public void mouseClicked(java.awt.event.MouseEvent evt) {
			if (evt.getSource() == imageLabel) {
				NekoM11.this.imageClicked(evt);
			}
		}

		public void mouseEntered(java.awt.event.MouseEvent evt) {
		}

		public void mouseExited(java.awt.event.MouseEvent evt) {
		}

		public void mousePressed(java.awt.event.MouseEvent evt) {
		}

		public void mouseReleased(java.awt.event.MouseEvent evt) {
		}
	}// </editor-fold>//GEN-END:initComponents

	private void imageClicked(java.awt.event.MouseEvent evt) {// GEN-FIRST:event_imageClicked
//		System.exit(0);//


		/**
		 * 不想要点击Neko就消失功能的把下面这句话注释掉。当然，你也可以改。
		 */
		this.dispose();//我把这里改成隐藏窗口，而不是退出程序



	}// GEN-LAST:event_imageClicked

	/**
	 * @param args the command line
	 *             arguments
	 * 下面的Main方法我注释掉了
	 */
//	public static void main(String args[]) {
//		java.awt.EventQueue.invokeLater(new Runnable() {
//			public void run() {
//				new NekoM11().setVisible(true);
//			}
//		});
//	}
	
	// Variables declaration - do not modify//GEN-BEGIN:variables
	private javax.swing.JLabel imageLabel;
	// End of variables declaration//GEN-END:variables

	private void loadKitten() {
		image = new ImageIcon[33];
		for (int i = 1; i <= 32; i++) {
			image[i] = new ImageIcon(NekoM11.class.getResource("images/" + i + ".GIF"));
		}
	}

	/** Locates the mouse on the screen and determines what the cat shall do. */
	private void locateMouseAndAnimateCat() {
		PointerInfo pointerInfo = MouseInfo.getPointerInfo();
		Point mouseLocation = pointerInfo.getLocation();

		int mx = mouseLocation.x;
		int my = mouseLocation.y;

		GraphicsConfiguration gc = getGraphicsConfiguration();
		Rectangle screenBounds = gc.getBounds();
		Insets screenInsets = getToolkit().getScreenInsets(gc);
		nekoBounds.x = screenBounds.x + screenInsets.left + 16;
		nekoBounds.y = screenBounds.y + screenInsets.top + 32;
		nekoBounds.width = screenBounds.width - screenInsets.left - screenInsets.right - 32;
		nekoBounds.height = screenBounds.height - screenInsets.left - screenInsets.top - 32;

		// Determines what the cat should do, if the mouse moves
		out = !nekoBounds.contains(mx, my);
		if (out) {
			x = mx;
			y = my;
			if (y < nekoBounds.y) {
				y = nekoBounds.y;
				pos = over;
			}
			if (y > nekoBounds.y + nekoBounds.height) {
				y = nekoBounds.y + nekoBounds.height;
				pos = under;
			}
			if (x < nekoBounds.x) {
				x = nekoBounds.x;
				pos = left;
			}
			if (x > nekoBounds.x + nekoBounds.width) {
				x = nekoBounds.x + nekoBounds.width;
				pos = right;
			}
		} else {
			move = (x != mx || y != my);
			x = mx;
			y = my;
			if (move) {
				slp = Math.min(slp, 200);
			}

		}
		dx = x - ox;
		dy = oy - y;
		dist = Math.sqrt(dx * dx + dy * dy); // distance formula (from mouse to cat)
		theta = Math.atan2(dy, dx); // angle from mouse to cat
		
		slp = Math.max(0, slp - timer.getDelay());
		if (slp == 0) {
			animateCat();
		}
	}

	private void animateCat() {
		
		if (dist > 16) { // moves cat 16 pixels
			slp = 200;
			ox = (int) (ox + Math.cos(theta) * 16);
			oy = (int) (oy - Math.sin(theta) * 16);
			dist = dist - 16;

			/*
			 * The following conditions determine what image should be shown. Remember there
			 * are two images for each action. For example if the cat's going right, display
			 * the cat with open legs and then with close legs, open, and so on.
			 */
			if (theta >= -pi / 8 && theta <= pi / 8) // right
			{
				no = (no == 5) ? 6 : 5;
			}
			if (theta > pi / 8 && theta < 3 * pi / 8) // upper-right
			{
				no = (no == 3) ? 4 : 3;
			}
			if (theta >= 3 * pi / 8 && theta <= 5 * pi / 8) // up
			{
				no = (no == 1) ? 2 : 1;
			}
			if (theta > 5 * pi / 8 && theta < 7 * pi / 8) // upper-left
			{
				no = (no == 15) ? 16 : 15;
			}
			if (theta >= 7 * pi / 8 || theta <= -7 * pi / 8) // left
			{
				no = (no == 13) ? 14 : 13;
			}
			if (theta > -7 * pi / 8 && theta < -5 * pi / 8) // bottom-left
			{
				no = (no == 11) ? 12 : 11;
			}
			if (theta >= -5 * pi / 8 && theta <= -3 * pi / 8) // down
			{
				no = (no == 9) ? 10 : 9;
			}
			if (theta > -3 * pi / 8 && theta < -pi / 8) // bottom-right
			{
				no = (no == 7) ? 8 : 7;
			}
			// sets move back to false
			move = false;
		} else { // -if the mouse hasn't moved or the cat's over the mouse-
			ox = x;
			oy = y;
			slp = 800;
			switch (no) {
			case 25: // <cat sit>
				// If the mouse is outside the applet
				if (out == true) {
					switch (pos) {
					case over:
						no = 17;
						break;
					case under:
						no = 21;
						break;
					case left:
						no = 23;
						break;
					case right:
						no = 19;
						break;
					default:
						no = 31;
						break;
					}
					pos = 0;
					break;
				}
				no = 31;
				break; // <31: cat lick>
			
			case 17: // The mouse is outside, above applet
				no = 18; // show images 17 & 18, 6 times
				ilc1++;
				if (ilc1 == 6) {
					no = 27;
					ilc1 = 0;
				}
				break;
			
			case 18:
				no = 17;
				break;
			
			case 21: // The mouse is outside, under applet
				no = 22; // show images 21 & 22, 6 times
				ilc1++;
				if (ilc1 == 6) {
					no = 27;
					ilc1 = 0;
				}
				break;
			
			case 22:
				no = 21;
				break;
			
			case 23: // the mouse is outside, left
				no = 24; // show images 23 & 24, 6 times
				ilc1++;
				if (ilc1 == 6) {
					no = 27;
					ilc1 = 0;
				}
				break;
			
			case 24:
				no = 23;
				break;
			
			case 19: // The mouse is outside, right
				no = 20; // show images 19 & 20, 6 times
				ilc1++;
				if (ilc1 == 6) {
					no = 27;
					ilc1 = 0;
				}
				break;
			
			case 20:
				no = 19;
				break;
			
			case 31: // cat lick (6 times)
				no = 25;
				ilc1++;
				if (ilc1 == 6) {
					no = 27;
					ilc1 = 0;
				}
				break;
			
			case 27:
				no = 28;
				break; // cat scratch (27 & 28, 4 times)
			case 28:
				no = 27;
				ilc2++;
				if (ilc2 == 4) {
					no = 26;
					ilc2 = 0;
				}
				break;
			case 26:
				no = 29;
				slp = 1600;
				break; // cat yawn (26)
			case 29:
				no = 30;
				slp = 1600;
				break; // cat sleep (29 & 30, forever)
			case 30:
				no = 29;
				slp = 1600;
				break;
			default:
				no = 25;
				break;
			}
			if (move == true) {
				// re-initialize some variables
				no = 32;
				ilc1 = 0;
				ilc2 = 0;
				move = false;
			}
		}
		if (init < 33) {
			// tells the user the program is testing the images, and tells them
			// when the test is done.
			slp = 200;
			ox = nekoBounds.x + nekoBounds.width / 2;
			oy = nekoBounds.y + nekoBounds.height / 2;
			no = init;
			init++;
		}
		// draw the new image
		setLocation(ox + windowOffset.x, oy + windowOffset.y);
		imageLabel.setIcon(image[no]);

	}
}