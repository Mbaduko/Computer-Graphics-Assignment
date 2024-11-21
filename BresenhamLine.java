import java.awt.*;
import javax.swing.*;

public class BresenhamLine extends JPanel {
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawLine(50, 50, 300, 200, g); // Example coordinates
    }

    private void drawLine(int x1, int y1, int x2, int y2, Graphics g) {
        int dx = Math.abs(x2 - x1);
        int dy = Math.abs(y2 - y1);
        int sx = x1 < x2 ? 1 : -1;
        int sy = y1 < y2 ? 1 : -1;

        int err = dx - dy;
        while (true) {
            g.fillRect(x1, y1, 1, 1); // Draw pixel
            if (x1 == x2 && y1 == y2) break;
            int e2 = 2 * err;
            if (e2 > -dy) {
                err -= dy;
                x1 += sx;
            }
            if (e2 < dx) {
                err += dx;
                y1 += sy;
            }
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.add(new BresenhamLine());
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}