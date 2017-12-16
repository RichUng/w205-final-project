CREATE VIEW latest_position AS
SELECT * FROM
(
  SELECT 
    RANK() OVER (PARTITION BY vehicle_id ORDER BY t_stamp DESC) AS order_number,
    A.vehicle_id,
    A.t_stamp,
    A.position_latitude,
    A.position_longitude,
    A.trip_id,
    A.agency,
    B.route_id,
    B.service_id,
    B.trip_headsign,
    B.direction_id,
    B.block_id,
    B.shape_id,
    C.name AS operator_name
  FROM vehicle_position A
  LEFT OUTER JOIN data_feed B ON TRIM(A.trip_id) = TRIM(B.trip_id)
  LEFT OUTER JOIN operator_list C ON TRIM(A.agency) = TRIM(C.id))
WHERE order_number = 1