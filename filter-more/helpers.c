#include "helpers.h"
#include <math.h>

// avr Gx Gy datastruct
typedef struct
{
    float rgbtRed;
    float rgbtGreen;
    float rgbtBlue;
} RGBTRIPLENOLIMIT;

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float total_value =
                (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue);
            int averaged_value = round(total_value / 3);
            image[i][j].rgbtRed = averaged_value;
            image[i][j].rgbtGreen = averaged_value;
            image[i][j].rgbtBlue = averaged_value;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE buffer[width];
    for (int i = 0; i < height; i++)
    {
        if (width % 2 == 0)
        {
            for (int j = 0; j < width / 2; j++)
            {
                buffer[j] = image[i][j];
                image[i][j] = image[i][width - 1 - j];
            }
            for (int j = (width / 2); j < width; j++)
            {
                image[i][j] = buffer[width - 1 - j];
            }
        }
        else
        {
            for (int j = 0; j < ((width - 1) / 2); j++)
            {
                buffer[j] = image[i][j];
                image[i][j] = image[i][width - 1 - j];
            }
            for (int j = ((width + 1) / 2); j < width; j++)
            {
                image[i][j] = buffer[width - 1 - j];
            }
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLENOLIMIT average;
    RGBTRIPLE imageb[height][width];

    // blurring centre pixels
    for (int i = 1; i < height - 1; i++)
    {
        for (int j = 1; j < width - 1; j++)
        {
            average.rgbtRed = 0;
            average.rgbtGreen = 0;
            average.rgbtBlue = 0;

            for (int a = i - 1; a <= i + 1; a++)
            {
                for (int b = j - 1; b <= j + 1; b++)
                {
                    average.rgbtRed += ((image[a][b].rgbtRed));
                    average.rgbtGreen += ((image[a][b].rgbtGreen));
                    average.rgbtBlue += ((image[a][b].rgbtBlue));
                }
            }

            imageb[i][j].rgbtRed = round(average.rgbtRed / 9);
            imageb[i][j].rgbtGreen = round(average.rgbtGreen / 9);
            imageb[i][j].rgbtBlue = round(average.rgbtBlue / 9);
        }
    }

    // blurring right edge pixels
    for (int i = 1; i < height - 1; i++)
    {
        average.rgbtRed = 0;
        average.rgbtGreen = 0;
        average.rgbtBlue = 0;

        for (int a = i - 1; a <= i + 1; a++)
        {
            for (int b = width - 2; b <= width - 1; b++)
            {
                average.rgbtRed += (image[a][b].rgbtRed);
                average.rgbtGreen += (image[a][b].rgbtGreen);
                average.rgbtBlue += (image[a][b].rgbtBlue);
            }
        }

        imageb[i][width - 1].rgbtRed = round(average.rgbtRed / 6);
        imageb[i][width - 1].rgbtGreen = round(average.rgbtGreen / 6);
        imageb[i][width - 1].rgbtBlue = round(average.rgbtBlue / 6);
    }

    // blurring left edge pixels
    for (int i = 1; i < height - 1; i++)
    {
        average.rgbtRed = 0;
        average.rgbtGreen = 0;
        average.rgbtBlue = 0;

        for (int a = i - 1; a <= i + 1; a++)
        {
            for (int b = 0; b <= 1; b++)
            {
                average.rgbtRed += ((image[a][b].rgbtRed));
                average.rgbtGreen += ((image[a][b].rgbtGreen));
                average.rgbtBlue += ((image[a][b].rgbtBlue));
            }
        }

        imageb[i][0].rgbtRed = round(average.rgbtRed / 6);
        imageb[i][0].rgbtGreen = round(average.rgbtGreen / 6);
        imageb[i][0].rgbtBlue = round(average.rgbtBlue / 6);
    }

    // blurring top edge pixels
    for (int j = 1; j < width - 1; j++)
    {
        average.rgbtRed = 0;
        average.rgbtGreen = 0;
        average.rgbtBlue = 0;

        for (int a = 0; a <= 1; a++)
        {
            for (int b = j - 1; b <= j + 1; b++)
            {
                average.rgbtRed += ((image[a][b].rgbtRed));
                average.rgbtGreen += ((image[a][b].rgbtGreen));
                average.rgbtBlue += ((image[a][b].rgbtBlue));
            }
        }

        imageb[0][j].rgbtRed = round(average.rgbtRed / 6);
        imageb[0][j].rgbtGreen = round(average.rgbtGreen / 6);
        imageb[0][j].rgbtBlue = round(average.rgbtBlue / 6);
    }

    // blurring bottom edge pixels
    for (int j = 1; j < width - 1; j++)
    {
        average.rgbtRed = 0;
        average.rgbtGreen = 0;
        average.rgbtBlue = 0;

        for (int a = height - 2; a <= height - 1; a++)
        {
            for (int b = j - 1; b <= j + 1; b++)
            {
                average.rgbtRed += ((image[a][b].rgbtRed));
                average.rgbtGreen += ((image[a][b].rgbtGreen));
                average.rgbtBlue += ((image[a][b].rgbtBlue));
            }
        }

        imageb[height - 1][j].rgbtRed = round(average.rgbtRed / 6);
        imageb[height - 1][j].rgbtGreen = round(average.rgbtGreen / 6);
        imageb[height - 1][j].rgbtBlue = round(average.rgbtBlue / 6);
    }

    // blurring top right corner pixels
    average.rgbtRed = 0;
    average.rgbtGreen = 0;
    average.rgbtBlue = 0;

    for (int a = 0; a <= 1; a++)
    {
        for (int b = width - 2; b <= width - 1; b++)
        {
            average.rgbtRed += ((image[a][b].rgbtRed));
            average.rgbtGreen += ((image[a][b].rgbtGreen));
            average.rgbtBlue += ((image[a][b].rgbtBlue));
        }
    }

    imageb[0][width - 1].rgbtRed = round(average.rgbtRed / 4);
    imageb[0][width - 1].rgbtGreen = round(average.rgbtGreen / 4);
    imageb[0][width - 1].rgbtBlue = round(average.rgbtBlue / 4);

    // blurring top left corner pixels
    average.rgbtRed = 0;
    average.rgbtGreen = 0;
    average.rgbtBlue = 0;

    for (int a = 0; a <= 1; a++)
    {
        for (int b = 0; b <= 1; b++)
        {
            average.rgbtRed += ((image[a][b].rgbtRed));
            average.rgbtGreen += ((image[a][b].rgbtGreen));
            average.rgbtBlue += ((image[a][b].rgbtBlue));
        }
    }

    imageb[0][0].rgbtRed = round(average.rgbtRed / 4);
    imageb[0][0].rgbtGreen = round(average.rgbtGreen / 4);
    imageb[0][0].rgbtBlue = round(average.rgbtBlue / 4);

    // blurring bottom right corner pixels
    average.rgbtRed = 0;
    average.rgbtGreen = 0;
    average.rgbtBlue = 0;

    for (int a = height - 2; a <= height - 1; a++)
    {
        for (int b = width - 2; b <= width - 1; b++)
        {
            average.rgbtRed += ((image[a][b].rgbtRed));
            average.rgbtGreen += ((image[a][b].rgbtGreen));
            average.rgbtBlue += ((image[a][b].rgbtBlue));
        }
    }

    imageb[height - 1][width - 1].rgbtRed = round(average.rgbtRed / 4);
    imageb[height - 1][width - 1].rgbtGreen = round(average.rgbtGreen / 4);
    imageb[height - 1][width - 1].rgbtBlue = round(average.rgbtBlue / 4);

    // blurring bottom left corner pixels
    average.rgbtRed = 0;
    average.rgbtGreen = 0;
    average.rgbtBlue = 0;

    for (int a = height - 2; a <= height - 1; a++)
    {
        for (int b = 0; b <= 1; b++)
        {
            average.rgbtRed += ((image[a][b].rgbtRed));
            average.rgbtGreen += ((image[a][b].rgbtGreen));
            average.rgbtBlue += ((image[a][b].rgbtBlue));
        }
    }

    imageb[height - 1][0].rgbtRed = round(average.rgbtRed / 4);
    imageb[height - 1][0].rgbtGreen = round(average.rgbtGreen / 4);
    imageb[height - 1][0].rgbtBlue = round(average.rgbtBlue / 4);

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = imageb[i][j].rgbtRed;
            image[i][j].rgbtGreen = imageb[i][j].rgbtGreen;
            image[i][j].rgbtBlue = imageb[i][j].rgbtBlue;
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLENOLIMIT Gx;
    RGBTRIPLENOLIMIT Gy;
    RGBTRIPLENOLIMIT sobel[height + 2][width + 2];

    // create new image with black border
    RGBTRIPLENOLIMIT images[height + 2][width + 2];

    for (int i = 0; i < height + 2; i++)
    {
        for (int j = 0; j < width + 2; j++)
        {
            images[i][j].rgbtRed = 0;
            images[i][j].rgbtGreen = 0;
            images[i][j].rgbtBlue = 0;
        }
    }

    for (int i = 1; i < height + 1; i++)
    {
        for (int j = 1; j < width + 1; j++)
        {
            images[i][j].rgbtRed = image[i - 1][j - 1].rgbtRed;
            images[i][j].rgbtGreen = image[i - 1][j - 1].rgbtGreen;
            images[i][j].rgbtBlue = image[i - 1][j - 1].rgbtBlue;
        }
    }

    // find Sobel Operator
    for (int i = 1; i < height + 1; i++)
    {
        for (int j = 1; j < width + 1; j++)
        {
            Gx.rgbtRed = 0;
            Gx.rgbtGreen = 0;
            Gx.rgbtBlue = 0;
            Gy.rgbtRed = 0;
            Gy.rgbtGreen = 0;
            Gy.rgbtBlue = 0;

            Gx.rgbtRed = (-1 * images[i - 1][j - 1].rgbtRed) + (1 * images[i - 1][j + 1].rgbtRed) +
                         (-2 * images[i][j - 1].rgbtRed) + (2 * images[i][j + 1].rgbtRed) +
                         (-1 * images[i + 1][j - 1].rgbtRed) + (1 * images[i + 1][j + 1].rgbtRed);

            Gy.rgbtRed = (-1 * images[i - 1][j - 1].rgbtRed) + (1 * images[i + 1][j - 1].rgbtRed) +
                         (-2 * images[i - 1][j].rgbtRed) + (2 * images[i + 1][j].rgbtRed) +
                         (-1 * images[i - 1][j + 1].rgbtRed) + (1 * images[i + 1][j + 1].rgbtRed);

            Gx.rgbtGreen =
                (-1 * images[i - 1][j - 1].rgbtGreen) + (1 * images[i - 1][j + 1].rgbtGreen) +
                (-2 * images[i][j - 1].rgbtGreen) + (2 * images[i][j + 1].rgbtGreen) +
                (-1 * images[i + 1][j - 1].rgbtGreen) + (1 * images[i + 1][j + 1].rgbtGreen);

            Gy.rgbtGreen =
                (-1 * images[i - 1][j - 1].rgbtGreen) + (1 * images[i + 1][j - 1].rgbtGreen) +
                (-2 * images[i - 1][j].rgbtGreen) + (2 * images[i + 1][j].rgbtGreen) +
                (-1 * images[i - 1][j + 1].rgbtGreen) + (1 * images[i + 1][j + 1].rgbtGreen);

            Gx.rgbtBlue = (-1 * images[i - 1][j - 1].rgbtBlue) +
                          (1 * images[i - 1][j + 1].rgbtBlue) + (-2 * images[i][j - 1].rgbtBlue) +
                          (2 * images[i][j + 1].rgbtBlue) + (-1 * images[i + 1][j - 1].rgbtBlue) +
                          (1 * images[i + 1][j + 1].rgbtBlue);

            Gy.rgbtBlue = (-1 * images[i - 1][j - 1].rgbtBlue) +
                          (1 * images[i + 1][j - 1].rgbtBlue) + (-2 * images[i - 1][j].rgbtBlue) +
                          (2 * images[i + 1][j].rgbtBlue) + (-1 * images[i - 1][j + 1].rgbtBlue) +
                          (1 * images[i + 1][j + 1].rgbtBlue);

            sobel[i][j].rgbtRed = sqrt(pow(Gx.rgbtRed, 2) + pow(Gy.rgbtRed, 2));

            if (sobel[i][j].rgbtRed > 255)
            {
                sobel[i][j].rgbtRed = 255;
            }
            sobel[i][j].rgbtGreen = sqrt(pow(Gx.rgbtGreen, 2) + pow(Gy.rgbtGreen, 2));
            if (sobel[i][j].rgbtGreen > 255)
            {
                sobel[i][j].rgbtGreen = 255;
            }
            sobel[i][j].rgbtBlue = sqrt(pow(Gx.rgbtBlue, 2) + pow(Gy.rgbtBlue, 2));
            if (sobel[i][j].rgbtBlue > 255)
            {
                sobel[i][j].rgbtBlue = 255;
            }
        }
    }

    for (int i = 1; i < height + 1; i++)
    {
        for (int j = 1; j < width + 1; j++)
        {
            image[i - 1][j - 1].rgbtRed = round(sobel[i][j].rgbtRed);
            image[i - 1][j - 1].rgbtGreen = round(sobel[i][j].rgbtGreen);
            image[i - 1][j - 1].rgbtBlue = round(sobel[i][j].rgbtBlue);
        }
    }

    return;
}
