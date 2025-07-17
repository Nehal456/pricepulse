{loading ? (
    <div className="text-center text-lg mt-4">🔄 Loading products...</div>
  ) : error ? (
    <div className="text-center text-red-500 mt-4">{error}</div>
  ) : products.length > 0 ? (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mt-4">
      {products.map((product, index) => (
        <div key={index} className="bg-white rounded-xl shadow-md p-4">
          <img src={product.image} alt={product.title} className="w-full h-48 object-contain mb-2" />
          <h2 className="text-lg font-semibold">{product.title}</h2>
          <p className="text-green-600 font-bold">{product.price}</p>
          <p className="text-sm text-gray-500">Source: {product.source}</p>
          <a href={product.link} target="_blank" rel="noopener noreferrer" className="text-blue-500 underline">View Product</a>
        </div>
      ))}
    </div>
  ) : (
    <p className="text-center mt-4">No products found.</p>
  )}
  