import java.awt.*;
import javax.swing.*;

public class BresenhamCircle extends JPanel {
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawCircle(200, 200, 100, g); // Example center and radius
    }

    private void drawCircle(int centerX, int centerY, int radius, Graphics g) {
        int x = 0;
        int y = radius;
        int d = 3 - 2 * radius; // Initial decision parameter

        while (y >= x) {
            // Draw the eight octants of the circle
            drawCirclePoints(centerX, centerY, x, y, g);
            x++;

            // Update decision parameter
            if (d > 0) {
                y--;
                d = d + 4 * (x - y) + 10; // Move to the next point in y
            } else {
                d = d + 4 * x + 6; // Move to the next point in x
            }
        }
    }
    
    private void drawCirclePoints(int centerX, int centerY, int x, int y, Graphics g) {
        g.fillRect(centerX + x, centerY + y, 1, 1);
        g.fillRect(centerX - x, centerY + y, 1, 1);
        g.fillRect(centerX + x, centerY - y, 1, 1);
        g.fillRect(centerX - x, centerY - y, 1, 1);
        g.fillRect(centerX + y, centerY + x, 1, 1);
        g.fillRect(centerX - y, centerY + x, 1, 1);
        g.fillRect(centerX + y, centerY - x, 1, 1);
        g.fillRect(centerX - y, centerY - x, 1, 1);
    }    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.add(new BresenhamCircle());
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}