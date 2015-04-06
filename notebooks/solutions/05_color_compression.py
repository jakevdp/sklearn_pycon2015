def compress_image(image, n_colors=64):
    """Compress an image

    Parameters
    ==========
    image : numpy array
        array of shape (height, width, 3) with integer values between 0 and 255
    n_colors : integer
        the number of colors in the final compressed image
        (i.e. the number of KMeans clusters to fit).
        
    Returns
    =======
    new_image : numpy array
        array representing the new image, compressed via KMeans clustering.
        It has the same shape and dtype as the input image, but contains
        only ``n_colors`` distinct colors.
    """
    X = image.reshape(-1, 3) / 255.
    model = KMeans(n_colors)
    labels = model.fit_predict(X)
    colors = model.cluster_centers_
    new_image = colors[labels].reshape(image.shape)
    return (255 * new_image).astype(np.uint8)


new_image = compress_image(china, 64)
plt.imshow(new_image);
