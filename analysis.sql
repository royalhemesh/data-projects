-- This SQL script analyzes the Olist e-commerce dataset to identify
-- high-revenue product categories and their corresponding average customer review scores.
-- It joins five key tables: orders, order_items, products, order_reviews, and product_category_name_translation.

-- CTE 1: Order_Items_Details
-- This CTE joins the orders and order_items tables.
-- It filters for delivered orders to ensure we only analyze completed transactions.
-- It links each product in an order with its price and order ID.
WITH Order_Items_Details AS (
    SELECT
        ord.order_id,
        item.product_id,
        item.price
    FROM
        olist_orders_dataset AS ord
    JOIN
        olist_order_items_dataset AS item
    ON
        ord.order_id = item.order_id
    WHERE
        ord.order_status = 'delivered'
),

-- CTE 2: Order_Reviews_Details
-- This CTE joins the results from the first CTE with the order_reviews table.
-- It attaches the customer review score to each product in a completed order.
Order_Reviews_Details AS (
    SELECT
        oid.order_id,
        oid.product_id,
        oid.price,
        rev.review_score
    FROM
        Order_Items_Details AS oid
    JOIN
        olist_order_reviews_dataset AS rev
    ON
        oid.order_id = rev.order_id
),

-- CTE 3: Product_Category_Details
-- This CTE joins the results from the second CTE with the products table.
-- It links each reviewed order item to its product category name.
Product_Category_Details AS (
    SELECT
        ord.product_id,
        ord.price,
        ord.review_score,
        prod.product_category_name
    FROM
        Order_Reviews_Details AS ord
    JOIN
        olist_products_dataset AS prod
    ON
        ord.product_id = prod.product_id
    WHERE
        prod.product_category_name IS NOT NULL
)

-- Final SELECT Statement
-- This query aggregates the data to the product category level.
-- It joins with the translation table to get the English category names.
-- It calculates the total revenue and average review score for each category.
-- The results are ordered by total revenue to easily identify the top-performing categories.
SELECT
    trans.product_category_name_english AS category,
    SUM(pcd.price) AS total_revenue,
    AVG(pcd.review_score) AS average_review_score
FROM
    Product_Category_Details AS pcd
JOIN
    product_category_name_translation AS trans
ON
    pcd.product_category_name = trans.product_category_name
GROUP BY
    category
ORDER BY
    total_revenue DESC;